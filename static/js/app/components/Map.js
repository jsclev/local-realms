import store from '../store/index.js?v=1'

Vue.component('Map', {
    store,
    data: function() {
        return {
            markerGroup: L.featureGroup()
        }
    },
    template: `
        <div>
            Showing {{ gameStores.length }} game stores.
        </div>`,
    mounted: function () {
        store.dispatch('businessList/getBusinesses', null, {root: true});
    },
    computed: {
        gameStores() {
            const gameStores = store.state.businessList.searchResults;

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
                marker.on('click', function onMarkerClick(e){
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
});
