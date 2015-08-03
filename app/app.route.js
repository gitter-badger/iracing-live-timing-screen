angular
    .module('iracing-live-timing-screen')
    .config(function ($stateProvider, $urlRouterProvider, $locationProvider) {
        'use strict';

        $urlRouterProvider.otherwise('/');

        $stateProvider
            .state('home', {
                url: "/",
                templateUrl: 'timing/layout.html',
                controller: 'timingController as timing'
            });
    });