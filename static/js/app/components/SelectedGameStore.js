import store from '../store/index.js?v=1'

Vue.component('SelectedGameStore', {
    store,
    template: `
        <div id="selected-game-store" 
             class=""
             v-if="selectedGameStore">
            <div>Name: {{ selectedGameStore.business.name }}</div>
            <div>Address: {{ selectedGameStore.street1 }} + {{ selectedGameStore.city }}</div>
            <div>Website: {{ selectedGameStore.business.website }}</div>
            <div>Email: {{ selectedGameStore.business.email }}</div>
            <div>Phone: {{ selectedGameStore.phone }}</div>
        </div>`,
    computed: {
        selectedGameStore() {
            return store.state.selectedGameStore;
        }
    }
});
