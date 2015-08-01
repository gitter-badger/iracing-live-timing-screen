angular
    .module('iracing-live-timing-screen')
    .config(function ($websocketProvider) {
        $websocketProvider.$setup({
            lazy: false,
            reconnect: false,
            reconnectInterval: 1000,
            mock: false,
            enqueue: false,
            //protocols: ['string']
        });
    });
