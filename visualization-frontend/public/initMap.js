function getIps(map) {
    const xhr = new XMLHttpRequest();
    const serverUrl = '/api'
    const query = { query: '{allConnections(last:1000){edges{node{sourceIp,credentials{edges{node{username,password}}}}}}}' };
    xhr.responseType = 'json';
    xhr.open('POST', serverUrl);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function () {
        let data = xhr.response.data.allConnections.edges.map(edge => {
            return edge.node;
        });
        let ip_info = data.reduce((acc, curr) => {
            const credentials = curr.credentials.edges.map(edge => edge.node);
            if (!acc.hasOwnProperty(curr.sourceIp)) {
                acc[curr.sourceIp] = { "credentials": [] };
            };
            credentials.forEach(cred => acc[curr.sourceIp].credentials.push(cred));
            return acc;
        }, {});

        let ips = Object.keys(ip_info);

        const xhr2 = new XMLHttpRequest();
        const serverUrl = '/geoip';
        xhr2.open('POST', serverUrl);
        xhr2.setRequestHeader('Content-Type', 'application/json');
        xhr2.onload = function () {
            JSON.parse(xhr2.response).forEach((latlon, idx) => {
                const ip = ips[idx];
                let marker = new google.maps.Marker({
                    position: latlon,
                    map: map,
                    title: ip
                });

                info = ip_info[ip];

                let info_window = new google.maps.InfoWindow({
                    content: '<div id="content">' +
                        '<div id="siteNotice">' +
                        '</div>' +
                        '<h1 id="firstHeading" class="firstHeading">' + ip + '</h1>' +
                        '<div id="bodyContent">' +
                        '<ul>' +
                        info.credentials.map(cred => `<li>${cred.username}:${cred.password}</li>`).join("") + 
                        '</ul>' +
                        '</div>' +
                        '</div>'
                });

                marker.addListener("click", () => {
                    info_window.open(map, marker);
                });
            });
        };
        xhr2.send(JSON.stringify(ips));
    };
    xhr.send(JSON.stringify(query));
}

let map;

function initMap() {
    let mapContainer = document.getElementById("map");
    if (mapContainer === null)
        return;
    map = new google.maps.Map(mapContainer, {
        zoom: 2,
        center: { lat: 0, lng: 0 }
    });
    getIps(map);
}
