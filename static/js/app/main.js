if ("geolocation" in navigator) {
    // console.log('geolocation available');
  /* geolocation is available */
} else {
  /* geolocation IS NOT available */
}

L.mapbox.accessToken = document.getElementById('mapboxAccessToken').value;
const map = L.mapbox.map('map')
    .setView([38.836684, -104.842041], 4)
    .addLayer(L.mapbox.styleLayer('mapbox://styles/mapbox/streets-v11'));
