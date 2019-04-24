import store from '../store/index.js';

new Vue({
    el: '#main-vue-hook',
    data: {
        searchString: null,
        markerGroup: L.featureGroup()
    },
    template: `
        <div id="main-panel">
            <input class="input-common input-common-default" 
                   placeholder="Search Local Game Stores" 
                   type="text" 
                   v-model="searchString" 
                   @keyup="search" />
            <div id="store-list" class="entity-list entity-list-default">
                <div v-for="business in filteredBusinesses" class="section-result-main">
                    <div class="section-result-icon"></div>
                    <div id="section-results-text" class="section-result">
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
            </div>
        </div>`,
    mounted() {
        store.dispatch('businessList/getBusinesses', null, {root: true});

        // var result_height = document.getElementById('section-results-text').style.height;
        // console.log(result_height);
        $('.section-result-icon').css('height', '80px');
        var header = $(".entity-list");
        var search = $(".input-common");
        $('#store-list').scroll(function () {
            var scroll = $('#store-list').scrollTop();


            if (scroll >= 10) {
                header.addClass("entity-list-transition");
                search.removeClass("input-common-default");

            } else {
                header.removeClass("entity-list-transition");
                search.addClass("input-common-default");
            }
        });

    },
    computed: {
        filteredBusinesses() {
            const filteredBusinesses = store.state.businessList.searchResults;

            map.removeLayer(this.markerGroup);

            let markers = [];

            for (let business of filteredBusinesses) {
                for (let gameStore of business.stores) {
                    let marker = L.marker([gameStore.lat, gameStore.lng]);
                    marker.bindPopup("<b>"+business.name+"</b><br>"+gameStore.street1+"<br>"+gameStore.city+", "+gameStore.stateCode);
                    markers.push(marker);
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
