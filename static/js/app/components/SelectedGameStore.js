import store from '../store/index.js?v=1'

Vue.component('SelectedGameStore', {
    store,
    template: `
        <div id="selected-game-store" 
             class=""
             v-if="selectedGameStore">
            <div>{{ selectedGameStore.business.name }}</div>
            <div class="info-list-container">
                <div class=""></div>
                <div class="info-text">
                    {{ selectedGameStore.street1 }}<br/>{{ selectedGameStore.city }}, {{ selectedGameStore.stateCode }} {{ selectedGameStore.zipCode }}
                </div>
            </div>
            <a :href="'http://' + selectedGameStore.business.website" target="_blank" style="text-decoration: none">
                <div id="website" class="info-list-container">
                    <div class="website-icon"></div> 
                    <span id="website-text" class="info-text">{{ selectedGameStore.business.website }}</span>
                </div>
            </a>
            <div class="info-list-container">
                <div class="info-text">
                    Email: {{ selectedGameStore.business.email }}
                </div>
            </div>
            <div class="info-list-container">
                <div class="info-text">
                    {{ selectedGameStore.phone }}
                </div>
            </div>
        </div>`,
    computed: {
        selectedGameStore() {
            return store.state.selectedGameStore;
        }
    }
});
