import Vue from 'vue'
import store from '../store/index.js'

export default Vue.component('Filters', {
    store,
    data: function () {
        return {
            errors: [],
            selectedTagIds: []
        }
    },
    template: `
        <div id="filters">
                <div v-for="tag in tags" class="tag-filter checked" :id="tag.name">
                    <button class="filter-item">{{ tag.name }}</button>
                    <div class="check-mark check-icon-show"></div>
                </div>
        </div>`,
    mounted: function () {
        store.dispatch('businessList/getTags', null, {root: true});

        const searchContainer = $("#input-container");
        const list = $(".entity-list");
        const searchOuter = $(".search-outer");

        $(document).ready(function () {
            var currentID;
            $('.tag-filter').click(function () {
                var currentID = this.id;
                currentID = $('[id="' + currentID + '"]');
                if ($(currentID).hasClass('checked')) {
                    $(currentID).removeClass('checked');
                    $(currentID).children('div').removeClass('check-icon-show');
                    $(currentID).children('button').css('color', 'rgba(0,0,0,.56)')
                } else {
                    $(currentID).addClass('checked');
                    $(currentID).children('div').addClass('check-icon-show');
                    $(currentID).children('button').css('color', 'rgba(0,0,0,.7)')
                }
            });
        });

        $('#filter-search').click(function () {
            if ($('#filters').hasClass('filter-expanded')) {
                $('#filters').removeClass('filter-expanded');
                list.removeClass("entity-list-transition-filter");
                searchContainer.removeClass("input-common-filter");
                searchOuter.removeClass("search-outer-after-filter");
                $('#filter-dim').removeClass('dimmed');
            } else {
                $('#filters').addClass('filter-expanded');
                list.addClass("entity-list-transition-filter");
                searchContainer.addClass("input-common-filter");
                searchOuter.addClass("search-outer-after-filter");
                $('#filter-dim').addClass('dimmed');
            }
        });
        $('#filter-dim').click(function () {
            $('#filters').removeClass('filter-expanded');
            list.removeClass("entity-list-transition-filter");
            searchContainer.removeClass("input-common-filter");
            searchOuter.removeClass("search-outer-after-filter");
            $('#filter-dim').removeClass('dimmed');
        })
    },
    computed:
        {
            tags: function () {
                const tags = store.state.businessList.tags;

                for (let tag of tags) {
                    this.selectedTagIds.push(tag.id);
                }

                return tags;
            }
            ,
        }
});
