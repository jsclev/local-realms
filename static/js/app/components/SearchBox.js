import store from '../store/index.js?v=1'

Vue.component('SearchBox', {
    store,
    data: function () {
        return {
            searchString: null
        }
    },
    template: `
        <div class="search-outer">
            <div id="input-container" class="input-common-default">
                <div class="menu-icon icon"></div>
                    <form id="search-form" autocomplete="off">
                        <input id="search-input" class="input-common"
                           placeholder="Find a local game store" 
                           type="text" 
                           v-model="searchString" 
                           @keyup="search" />
                            <div id="main-search-icon" class="search-icon icon"/>
                    </form>
                    <hr id="search-separator">
                    <div id="filter-search" class="icon"/>
            </div>
        </div>`,
    mounted: function () {
        $("#main-search-icon").click(function () {
                const search = $('#search-input');

                if (search.val()) {
                    $('#search-form').submit();
                    event.preventDefault();
                } else {
                    search.focus();
                    event.preventDefault();
                }
            }
        );

        $('#search-form').submit(function () {
            alert("Handler for .submit() called.");
            event.preventDefault();
            return false;
        });
    },
    computed: {
        tags: function () {
            if (store.state.businessList.isLoadingTags) {
                return [];
            }

            const tags = store.state.businessList.tags;

            for (let tag of tags) {
                this.selectedTagIds.push(tag.id);
            }

            return tags;
        },
    },
    methods: {
        search() {
            store.dispatch('selectedStore/select', null, {root: true});
            store.dispatch('businessList/search', this.searchString, {root: true});
        }
    }
});
