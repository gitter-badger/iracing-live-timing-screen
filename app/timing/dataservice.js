angular
    .module('iracing-live-timing-screen')
    .factory('timingFactory', timingFactory);

function timingFactory ($q) {
    return {
        getStandings: function (vm) {
            return vm;
        },

        drivers: []
    };
}
