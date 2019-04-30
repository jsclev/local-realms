import store from '../store/index.js?v=0.0.2'

Vue.component('SelectedGameStore', {
    store,
    template: `
        <div id="selected-game-store" 
             class="selected-game-store-closed"
             v-if="selectedGameStore">
            <div id="info-header">
                <div style="display: flex;justify-content: center;flex-direction: column;">{{ selectedGameStore.business.name }}</div>
                <div id="up-down-icon" class="icon up-icon-position"></div>
            </div>
            <a :href="'https://www.google.com/maps/place/' + selectedGameStore.street1 + ' ' + selectedGameStore.city + ' ' + selectedGameStore.stateCode + ' ' + selectedGameStore.zipCode" target="_blank" style="text-decoration: none">
                <div class="info-list-container tooltip">
                    <div id="place-info-icon" class="info-icon"></div>
                    <div class="info-text">
                        {{ selectedGameStore.street1 }}<br/>{{ selectedGameStore.city }}, {{ selectedGameStore.stateCode }} {{ selectedGameStore.zipCode }}
                    </div>
                    <span class="tooltiptext">Google Maps</span>
                </div>
            </a>
            
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
        </div>
        <div id="selected-game-store" v-else="" class="selected-game-store-closed">
            <div id="info-header">
            <div style="display: flex;justify-content: center;flex-direction: column;">Select a store</div>
            <div id="up-down-icon" class="icon up-icon-position"></div>
            </div>
            <br/>
            <span style="font-size: 15px; color: #656565; margin-left: 3px">Select a store from the store list to see information</span>
        </div>`,
    mounted: function () {
        $(document).ready(function () {
            $('#up-down-icon').click(function () {
                if ($('#selected-game-store').hasClass('selected-game-store-closed')) {
                    $('#selected-game-store').removeClass('selected-game-store-closed');
                    $('#up-down-icon').removeClass('up-icon-position')


                } else {
                    $('#selected-game-store').addClass('selected-game-store-closed');
                    $('#up-down-icon').addClass('up-icon-position');
                }
            });
        });

    },
    computed: {
        selectedGameStore() {

            return store.state.selectedGameStore;
        },
    },
});
