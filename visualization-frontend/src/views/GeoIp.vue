<template>
  <div class="geoip">
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
