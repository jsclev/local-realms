import store from '../store/index.js';

new Vue({
    el: '#main-vue-hook',
    data: {
        searchString: null,
        markerGroup: L.featureGroup()
    },
    template: `
        <div id="main-panel">
            <div id="menu">
                <div class="header">
                    <div id="menu-back-icon" class="icon"></div>
                </div>
            </div>
            <div class="search-outer">
                <div id="input-container" class="input-common-default">
                    <div class="menu-icon icon"></div>
                        <form id="search-form" autocomplete="off">
                            <input id="search-input" class="input-common"
                               placeholder="Search Local Game Stores" 
                               type="text" 
                               v-model="searchString" 
                               @keyup="search" />
                                <div id="main-search-icon" class="search-icon icon"/>
                        </form>
                </div>
            </div>
<!--            <div id="message">Start typing in the search box to search local game stores</div>-->
            <div id="store-list" class="entity-list entity-list-default">
                <div v-for="store in filteredStores" class="section-result-main">
                    <div class="section-result-icon"></div>
                    <div id="section-results-text" class="section-result">
                        <div class="section-result-title">
                            {{ store.business.name }}
                        </div>
                    </div>
                </div>
            </div>
        </div>`,
    mounted() {
        store.dispatch('businessList/getBusinesses', null, {root: true});

        $('.menu-icon').click(function () {
            $('#menu').addClass('menu-open');
            $('#map').addClass('dim');
            $('#store-list').addClass('dim');
            $('.search-outer').addClass('dim');
            $('#menu-back-icon').addClass('back-icon');

        });
        $('#menu-back-icon').click(function () {
            $('#menu').removeClass('menu-open');
            $('#map').removeClass('dim');
            $('#store-list').removeClass('dim');
            $('.search-outer').removeClass('dim');
            $('#menu-back-icon').removeClass('back-icon');

        });
        $("#main-search-icon").click(function () {
                const search = $('#search-input');

                if (search.val()) {
                    $('#search-form').submit();
                    event.preventDefault();
                }
                else {
                    search.focus();
                    event.preventDefault();
                }
            }
        );
        $('#search-form').submit(function () {
            alert( "Handler for .submit() called." );
            event.preventDefault();
            return false;
        });

        const searchContainer = $("#input-container");
        const list = $(".entity-list");
        const searchOuter = $(".search-outer");
        $('#store-list').scroll(function () {
            var scroll = $('#store-list').scrollTop();


            if (scroll >= 10) {
                list.addClass("entity-list-transition");
                searchContainer.removeClass("input-common-default");
                searchOuter.addClass("search-outer-after")

            } else {
                list.removeClass("entity-list-transition");
                searchContainer.addClass("input-common-default");
                searchOuter.removeClass("search-outer-after")
            }
        });


    },
    computed: {
        filteredStores() {
            const filteredBusinesses = store.state.businessList.searchResults;

            // map.removeLayer(this.markerGroup);
            //
            // let markers = [];
            //
            // for (let business of filteredBusinesses) {
            //     for (let gameStore of business.stores) {
            //         markers.push(L.marker([gameStore.lat, gameStore.lng]));
            //     }
            // }
            //
            // this.markerGroup = L.featureGroup(markers);
            // this.markerGroup.addTo(map);

            return filteredBusinesses;
        }
    },
    methods: {
        search() {
            store.dispatch('businessList/search', this.searchString, {root: true});
        }
    }
});
