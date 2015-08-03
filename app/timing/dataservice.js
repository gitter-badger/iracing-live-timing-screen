angular
    .module('iracing-live-timing-screen')
    .service('timingService', timingService);

function timingService($websocket) {

    this.connect = function(url) {
        this.ws = $websocket.$new('ws://' + url)
    };

    this.getStandings = function() {
        var drivers = [];
        this.ws.$emit('standings', 'i need some standings');
        this.ws.$on('ping', function (data) {
            data.forEach(function (item) {
                drivers.push(item);
            });
            return drivers;
        });
    };
}