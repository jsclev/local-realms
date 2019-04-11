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
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "saturation": 36
            },
            {
                "color": "#000000"
            },
            {
                "lightness": 40
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#000000"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "on"
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 17
            },
            {
                "weight": 1.2
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 21
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#00ff00"
            },
            {
                "lightness": 17
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 29
            },
            {
                "weight": 0.2
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 18
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 19
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#000000"
            },
            {
                "lightness": 17
            }
        ]
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
