<template>
    <div id="number-results">
        <div class="margin-auto">{{ gameStores.length }} locations</div>
        <hr class="search-separator" style="margin: 8px 0 8px !important;">
        <div class="margin-auto">Local Realms</div>
        <button class="margin-auto new-store-button" @click="create">New Store</button>
    </div>
</template>

<script>
    import store from '../store/index'

    export default {
        data: function () {
            return {
                markerGroup: L.featureGroup(),
                userLocationMarker: L.marker()
            }
        },
        created: function() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(this.markUserLocation);
            }

        },
        mounted: function () {
            store.dispatch('businessList/getBusinesses', null, {root: true});
            store.dispatch('businessList/setGeographicBounds', map.getBounds(), {root: true});

            // Attach map bounds change handler
            map.on('moveend', function (e) {
                store.dispatch('businessList/setGeographicBounds', map.getBounds(), {root: true});
            });
        },
        computed: {
            gameStores() {
                const gameStores = store.getters['businessList/filteredStores'];

                map.removeLayer(this.markerGroup);
                let markers = [];

                for (let gameStore of gameStores) {
                    const latLng = L.latLng(gameStore.lat, gameStore.lng);
                    const options = {
                        radius: 8,
                        color: '#fff',
                        weight: 1,
                        opacity: 1.0,
                        fill: true,
                        fillColor: '#0593c4',
                        fillOpacity: 1.0
                    };

                    const marker = L.circleMarker(latLng, options);
                    marker.bindPopup(this.getPopupHtml(gameStore));
                    marker.on('click', function onMarkerClick(e) {
                        store.dispatch('setSelectedGameStore', gameStore, {root: true});
                    });
                    markers.push(marker);
                }

                this.markerGroup = L.featureGroup(markers);
                this.markerGroup.addTo(map);

                return gameStores;
            }
        },
        methods: {
            create() {
                store.dispatch('setIsCreatingNewStore', true, {root: true})
            },
            getPopupHtml(gameStore) {
                let html = "<b>";
                html += gameStore.business.name;
                html += '</b><br>';
                html += gameStore.address1;
                html += '<br>';
                html += gameStore.city + ", " + gameStore.stateCode;

                return html;
            },
            markUserLocation(location){
                let lat = location.coords.latitude;
                let lng = location.coords.longitude;
                const latLng = L.latLng(lat, lng);
                const marker = L.marker(latLng);
                marker.bindPopup("Your Location");
                marker.addTo(map);
                map.setView(latLng, 9)
            }
        }
    }
</script>

<style scoped>
    .margin-auto {
        margin: auto;
    }

    .new-store-button {
        background-color: white;
        border: none;
        color: #8f8f8f;
    }
</style>

