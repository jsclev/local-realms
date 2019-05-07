<template>
    <div id="store-list" class="entity-list entity-list-default">
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
            const searchContainer = $("#input-container");
            const list = $(".entity-list");
            const searchOuter = $(".search-outer");

            $('#store-list').scroll(function () {
                const scroll = $('#store-list').scrollTop();

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
            },
        }
    }
</script>

<style scoped>
    #store-list {
        background-color: transparent;
        overflow-y: auto;
    }

    .entity-list {
        height: 100%;
        -webkit-transition: ease 250ms;
        -moz-transition: ease 250ms;
        -ms-transition: ease 250ms;
        -o-transition: ease 250ms;
        transition: ease 250ms;
        border-top: white 0 solid;
        flex: 0 1 auto;
        -ms-overflow-style: none;
        overflow: -moz-scrollbars-none;
    }

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
