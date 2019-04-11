import storeList from './modules/StoreList.js'
// import accountUser from './modules/account-user/account-user.js?v=3.11.4'
// import clientDetails from './modules/clients/client-details.js?v=3.11.4'
// import dayList from './modules/routes/dayList.js?v=3.11.4'
// import community from './modules/community/community.js?v=3.11.4'
// import mealVerificationList from './modules/operations/meal-verifications.js?v=3.11.4'
// import reportDialogs from './modules/reports/report-dialogs.js?v=3.11.4'
// import routeSheetsJob from './modules/routes/route-sheets-job.js?v=3.11.4'
// import volunteerDetails from './modules/volunteers/volunteer-details.js?v=3.11.4'

export default new Vuex.Store({

    modules: {
        storeList: storeList
    }
});
