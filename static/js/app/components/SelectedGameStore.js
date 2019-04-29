import store from '../store/index.js?v=0.0.2'

Vue.component('SelectedGameStore', {
    store,
    template: `
        <div id="selected-game-store" 
             class=""
             v-if="selectedGameStore">
            <div id="info-header">{{ selectedGameStore.business.name }}</div>
            <div class="info-list-container">
                <div id="place-info-icon" class="info-icon"></div>
                <div class="info-text">
                    {{ selectedGameStore.street1 }}<br/>{{ selectedGameStore.city }}, {{ selectedGameStore.stateCode }} {{ selectedGameStore.zipCode }}
                </div>
            </div>
            <a :href="'http://' + selectedGameStore.business.website" target="_blank" style="text-decoration: none">
                <div id="website" class="info-list-container">
                    <div id="website-icon" class="info-icon"></div> 
                    <span id="website-text" class="info-text">{{ selectedGameStore.business.website }}</span>
                </div>
            </a>
            <div class="info-list-container">
                <div id="email-icon" class="info-icon"></div>
                <div class="info-text">
                    {{ selectedGameStore.business.email }}
                </div>
            </div>
            <div class="info-list-container">
                <div id="phone-icon" class="info-icon"></div>
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
