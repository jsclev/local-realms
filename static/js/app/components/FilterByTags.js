import store from '../store/index.js?v=1'

Vue.component('FilterByTags', {
    store,
    data: function() {
        return {
            errors: [],
            selectedTagIds: []
        }
    },
    template: `
        <div id="tag-filters">
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
    },
    computed: {
        tags: function() {
            if (store.state.businessList.isLoadingTags) {
                return [];
            }

            const tags = store.state.businessList.tags;

            for (let tag of tags) {
                this.selectedTagIds.push(tag.id);
            }

            return tags;
        },
    }
});
