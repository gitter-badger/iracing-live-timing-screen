angular
    .module('iracing-live-timing-screen')
    .controller('timingController', timingController);

function timingController($websocket) {
    var vm = this;

    var ws = $websocket.$new('ws://localhost:9997');
    ws.$on('$open', function() {
        console.log('Websocket is open!');
        ws.$emit('ping', 'hi server');
    })
}
