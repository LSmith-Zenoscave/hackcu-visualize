<template>
  <div class="geoip">
    Click on a point to view credentials attempted by that ip at that location.
    <div id="map" />
  </div>
</template>
<script>
/* global initMap */
export default {
  data: () => ({}),
  mounted() {
    initMap();
  },
  methods: {}
};
</script>
<style scoped>
.geoip {
  min-height: 640px;
}

#map {
  height: 640px;
}
</style>
