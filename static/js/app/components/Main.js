import store from '../store/index.js';

new Vue({
    el: '#main-vue-hook',
    template: `
        <div id="main-panel">
            <ul id="reports-list-container" class="entity-list">
                <li v-for="store in stores">
                    {{ store.name }}
                </li>
            </ul>
        </div>`,
    mounted() {
        store.dispatch('storeList/getStores', null, {root: true});

        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 39.833333, lng: -98.583333},
            zoom: 5,
            mapTypeControl: false,
            styles: [
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#0B1E0C"
                        },
                        {
                            "saturation": 2
                        },
                        {
                            "lightness": -89
                        },
                        {
                            "visibility": "simplified"
                        }
                    ]
                },
                {
                    "featureType": "landscape.man_made",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#0B1E0C"
                        },
                        {
                            "saturation": 26
                        },
                        {
                            "lightness": -91
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "landscape.natural",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#0B1E0C"
                        },
                        {
                            "saturation": 37
                        },
                        {
                            "lightness": -92
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#0B1E0C"
                        },
                        {
                            "saturation": 6
                        },
                        {
                            "lightness": -90
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "landscape.man_made",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#0B1E0C"
                        },
                        {
                            "saturation": 26
                        },
                        {
                            "lightness": -91
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "road",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -22
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "road.highway",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -22
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "road.arterial",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -35
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "road.local",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -50
                        },
                        {
                            "visibility": "on"
                        }
                    ]
                },
                {
                    "featureType": "administrative",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -2
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi.park",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -36
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "administrative.locality",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": 50
                        },
                        {
                            "visibility": "simplified"
                        }
                    ]
                },
                {
                    "featureType": "poi",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -36
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "poi.place_of_worship",
                    "elementType": "all",
                    "stylers": [
                        {
                            "hue": "#00FF00"
                        },
                        {
                            "saturation": 100
                        },
                        {
                            "lightness": -41
                        },
                        {
                            "visibility": "off"
                        }
                    ]
                },
                {
                    "featureType": "water",
                    "elementType": "all",
                    "stylers": []
                }
            ]
        });
    },
    computed: {
        stores() {
            const stores = store.state.storeList.stores;

            for (let gameStore of stores) {
                for (let postalAddress of gameStore.postalAddresses) {
                    const location = {
                        lat: parseFloat(postalAddress.lat),
                        lng: parseFloat(postalAddress.lng)
                    };

                    new google.maps.Marker({
                        position: location,
                        map: map,
                        title: gameStore.name,
                        icon: 'static/images/map-pin-04.png',
                    });
                }

            }

            return store.state.storeList.stores;
        }
    },
    methods: {
        openDialog: function (prefix) {
            $('#' + prefix + '-dialog').dialog('open');
        }
    }
});
