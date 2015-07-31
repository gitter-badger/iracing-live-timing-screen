angular
    .module('iracing-live-timing-screen')
    .run(function($websocket){
        var ws = $websocket.$new({
            url: 'ws://localhost:8765',
            lazy: false
        })
            .$on('$open', function() {
                console.log($ws.$status());
            });
    });