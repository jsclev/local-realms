import store from '../store/index.js';

new Vue({
    el: '#main-vue-hook',
    data: {
        searchString: null,
        markers: []
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

        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 38.836684, lng: -104.842041},
            zoom: 4,
            mapTypeControl: false,
            // styles: [
            //     {
            //         "featureType": "water",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#0B1E0C"
            //             },
            //             {
            //                 "saturation": 2
            //             },
            //             {
            //                 "lightness": -89
            //             },
            //             {
            //                 "visibility": "simplified"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "landscape.man_made",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#0B1E0C"
            //             },
            //             {
            //                 "saturation": 26
            //             },
            //             {
            //                 "lightness": -91
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "landscape.natural",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#0B1E0C"
            //             },
            //             {
            //                 "saturation": 37
            //             },
            //             {
            //                 "lightness": -92
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "poi.park",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#0B1E0C"
            //             },
            //             {
            //                 "saturation": 6
            //             },
            //             {
            //                 "lightness": -90
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "landscape.man_made",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#0B1E0C"
            //             },
            //             {
            //                 "saturation": 26
            //             },
            //             {
            //                 "lightness": -91
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "road",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -22
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "road.highway",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -22
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "road.arterial",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -35
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "road.local",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -50
            //             },
            //             {
            //                 "visibility": "on"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "administrative",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -2
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "poi.park",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -36
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "administrative.locality",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": 50
            //             },
            //             {
            //                 "visibility": "simplified"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "poi",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -36
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "poi.place_of_worship",
            //         "elementType": "all",
            //         "stylers": [
            //             {
            //                 "hue": "#00FF00"
            //             },
            //             {
            //                 "saturation": 100
            //             },
            //             {
            //                 "lightness": -41
            //             },
            //             {
            //                 "visibility": "off"
            //             }
            //         ]
            //     },
            //     {
            //         "featureType": "water",
            //         "elementType": "all",
            //         "stylers": []
            //     }
            // ]
        });


    },
    computed: {
        filteredBusinesses() {
            const filteredBusinesses = store.state.businessList.searchResults;

            // Clear existing markers
            for (let marker of this.markers) {
                marker.setMap(null);
            }

            for (let business of filteredBusinesses) {
                for (let gameStore of business.stores) {
                    const location = {
                        lat: parseFloat(gameStore.lat),
                        lng: parseFloat(gameStore.lng)
                    };

                    this.markers.push(new google.maps.Marker({
                        position: location,
                        map: map,
                        title: business.name,
                        icon: 'static/images/marker.png',
                    }));
                }

            }

            return filteredBusinesses;
        }
    },
    methods: {
        search() {
            store.dispatch('businessList/search', this.searchString, {root: true});
        }
    }
});
