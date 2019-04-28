import store from '../store/index.js?v=1'

Vue.component('Filters', {
    store,
    data: function() {
        return {
            errors: [],
            selectedTagIds: []
        }
    },
    template: `
        <div id="filters">
                <div v-for="tag in tags" class="tag-filter">
                    <input type="checkbox"
                           :id="tag.id"
                           :value="tag.id"
                           v-model="selectedTagIds">
                    <label :for="tag.id">{{ tag.name }}</label>
                </div>
        </div>`,
    mounted: function () {
        store.dispatch('businessList/getTags', null, {root: true});

        const searchContainer = $("#input-container");
        const list = $(".entity-list");
        const searchOuter = $(".search-outer");

        $('#filter-search').click(function () {
            if ($('#filters').hasClass('filter-expanded')) {
                $('#filters').removeClass('filter-expanded');
                list.removeClass("entity-list-transition-filter");
                searchContainer.removeClass("input-common-filter");
                searchOuter.removeClass("search-outer-after-filter")
            }
            else {
                $('#filters').addClass('filter-expanded');
                list.addClass("entity-list-transition-filter");
                searchContainer.addClass("input-common-filter");
                searchOuter.addClass("search-outer-after-filter")
            }
        });
    },
    computed: {
        tags: function() {
            const tags = store.state.businessList.tags;

            for (let tag of tags) {
                this.selectedTagIds.push(tag.id);
            }

            return tags;
        },
    }
});
