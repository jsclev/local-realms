import store from '../store/index.js';

new Vue({
    el: '#main-vue-hook',
    data: {
        searchString: null,
        markerGroup: L.featureGroup()
    },
    template: `
        <div id="main-panel">
            <input class="input-common" 
                   placeholder="Search Local Game Stores" 
                   type="text" 
                   v-model="searchString" 
                   @keyup="search" />
            <div id="store-list" class="entity-list">
                <div v-for="business in filteredBusinesses" class="section-result">
                    <div class="section-result-title">
                        {{ business.name }}
                    </div>
                    <div v-for="store in business.stores" class="section-result-details">
                        <span v-if="store.name">
                            {{ store.name }}, {{ store.street1 }}, {{ store.city }} {{ store.stateCode }}
                        </span>
                        <span v-else>
                            {{ store.street1 }}, {{ store.city }} {{ store.stateCode }}
                        </span>
                    </div>
                </div>
            </div>
        </div>`,
    mounted() {
        store.dispatch('businessList/getBusinesses', null, {root: true});
    },
    computed: {
        filteredBusinesses() {
            const filteredBusinesses = store.state.businessList.searchResults;

            map.removeLayer(this.markerGroup);

            let markers = [];

            for (let business of filteredBusinesses) {
                for (let gameStore of business.stores) {
                    markers.push(L.marker([gameStore.lat, gameStore.lng]));
                }
            }

            this.markerGroup = L.featureGroup(markers);
            this.markerGroup.addTo(map);

            return filteredBusinesses;
        }
    },
    methods: {
        search() {
            store.dispatch('businessList/search', this.searchString, {root: true});
        }
    }
});
