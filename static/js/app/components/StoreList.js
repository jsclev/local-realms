import store from '../store/index.js?v=1'

Vue.component('StoreList', {
    store,
    template: `
        <div id="store-list" class="entity-list entity-list-default">
            <div v-for="store in gameStores" class="section-result-main">
                <div class="section-result-icon"></div>
                <div id="section-results-text" class="section-result">
                    <div class="section-result-title">
                        {{ store.business.name }}
                    </div>
                    <div class="section-result-details">
                        {{ store.city }}, {{ store.stateCode }}
                    </div>
                </div>
            </div>
        </div>`,
    mounted: function () {
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
        gameStores() {
            return store.state.businessList.searchResults;
        }
    },
    methods: {
        getStoreText(gameStore) {
            // let score = '';
            //
            // if (gameStore.searchResult && gameStore.searchResult.score !== null) {
            //     score = '(' + gameStore.searchResult.score.toPrecision(4) + ')';
            // }

            return gameStore.business.name;
        }
    }
});
