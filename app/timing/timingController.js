angular
    .module('iracing-live-timing-screen')
    .controller('timingController', timingController);

function timingController($websocket) {
    var vm = this;
    var ws = $websocket.$new('ws://localhost:8765');

    ws.$on('$open', function (data) {
        ws.$emit('ping','Martin Kronke');
        console.log(ws.$status());
    });

    ws.$on('ping', function (data) {
        var drivers = [];
        data.forEach(function (item, index, array) {
            drivers.push(item);
        });
        vm.drivers = drivers;
        console.log(vm.drivers);
    });
}