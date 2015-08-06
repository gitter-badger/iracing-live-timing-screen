angular
    .module('iracing-live-timing-screen')
    .controller('timingController', timingController);

function timingController($websocket, timingFactory, $scope) {
    var vm = this;
    timing = timingFactory;
    var ws = $websocket.$new('ws://localhost:8765');

    ws.$on('$open', function (data) {
        ws.$emit('ping','Martin Kronke');
        console.log('Connection:' + ws.$status());
    });

    ws.$on('getStandings', function (data) {
        data.forEach(function (item) {
            timing.drivers.push(item);
        });
        console.log(timing.drivers);
        vm.drivers = timing.drivers;
        $scope.$apply();
    });



}