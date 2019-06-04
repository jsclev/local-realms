<template>
    <div>
        <div style="height: 68px; width: 100%"></div>
        <div v-for="store in gameStores"
             class="section-result-main"
             :class="{ selectedStoreListItem: isSelected(store) }"
             @click="selectGameStore(store)">
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
    </div>
</template>

<script>
    import store from '../store/index'

    export default {
        mounted: function () {
            // const searchContainer = $("#input-container");
            // const list = $(".entity-list");
            // const searchOuter = $(".search-outer");
            //
            // $('#store-list').scroll(function () {
            //     const scroll = $('#store-list').scrollTop();
            //
            //     if (scroll >= 10) {
            //         list.addClass("entity-list-transition");
            //         searchContainer.removeClass("input-common-default");
            //         searchOuter.addClass("search-outer-after")
            //
            //     } else {
            //         list.removeClass("entity-list-transition");
            //         searchContainer.addClass("input-common-default");
            //         searchOuter.removeClass("search-outer-after")
            //     }
            // });
        },
        computed: {
            gameStores() {
                return store.getters['businessList/filteredStores'];
            }
        },
        methods: {
            isSelected(gameStore) {
                if (store.state.selectedGameStore && store.state.selectedGameStore.id === gameStore.id) {
                    return true;
                }

                return false;
            },
            selectGameStore(gameStore) {
                store.dispatch('setSelectedGameStore', gameStore, {root: true});
                const latLng = L.latLng(gameStore.lat, gameStore.lng);
                var popup = new L.Popup({closeOnClick: false})
                    .setLatLng(latLng)
                    .setContent(this.getPopupHtml(gameStore))
                    .openOn(map);
                console.log('test');
            },
             getPopupHtml(gameStore) {
                 let html = "<b>";
                 html += gameStore.business.name;
                 html += '</b><br>';
                 html += gameStore.address1;
                 html += '<br>';
                 html += gameStore.city + ", " + gameStore.stateCode;

                 return html;
             }
        }
    }
</script>

<style scoped>




    .section-result {
        display: inline-block;
        width: 85%;
        padding: 14px 0 14px 6px;
        height: 100%;
    }

    .section-result-main {
        display: flex;
        align-items: center;
        border-bottom: #f2f2f2 1px solid;
    }

    .section-result-main:hover {
        background-color: #f9f9f9;
    }

    .section-result-title {
        font-size: 18px;
    }

    .section-result-details {
        font-size: 11px;
        color: dimgray;
    }


</style>
