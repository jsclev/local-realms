<template>
    <div id="number-results">
        <div style="margin: auto;">{{ gameStores.length }} locations</div>
        <hr class="search-separator" style="margin: 8px 0 8px !important;">
        <div style="margin: auto">Local Realms</div>
    </div>
</template>

<script>
    import store from '../store/index'

    export default {
        data: function () {
            return {
                markerGroup: L.featureGroup()
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
            getPopupHtml(gameStore) {
                let html = "<b>";
                html += gameStore.business.name;
                html += '</b><br>';
                html += gameStore.street1;
                html += '<br>';
                html += gameStore.city + ", " + gameStore.stateCode;

                return html;
            }
        }
    }
</script>
