goog.provide('main.main');


/**
 * @suppress {checkTypes}
 */
main.main = function($, Highcharts) {
    var series = {error: null, warning: null, lint: null};
    var data_x = 0;
    var prev_when;
    $(document).ready(function() {
        function set_series(name, value) {
            series[name] = value;
        }

        setInterval(function() {
            if (series['error'] && series['warning'] && series['lint']) {
                $.getJSON('/api/get', function(data) {
                    var when = data['when'];
                    if (when != prev_when) {
                        data_x++;
                        series['error'].addPoint(
                            [data_x, data['error']], true, true);
                        series['warning'].addPoint(
                            [data_x, data['warning']], true, true);
                        series['lint'].addPoint(
                            [data_x, data['lint']], true, true);
                        prev_when = when;
                        if (!data['success']) {
                            $('#border').css('border-color', 'red')
                            .css('background', '#FFAAAA');
                        }else {
                            $('#border').css('background', 'white');
                            if (data['warning'] > 0) {
                                $('#border').css('border-color', 'yellow');
                            }else {
                                $('#border').css('border-color', 'green');
                            }
                        }
                    }
                });
            }
        }, 1000);


        function add_graph(target, title) {
            var chart;
            chart = new Highcharts.Chart({
                chart: {
                    renderTo: target,
                    type: 'line',
                    marginRight: 10,
                    events: {
                        load: function() {
                            set_series(target, this.series[0]);
                        }
                    }
                },
                title: {
                    text: title
                },
                xAxis: {
                    tickPixelInterval: 150
                },
                yAxis: {
                    title: {
                        text: 'Value'
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#908080'
                    }]
                },
                tooltip: {
                    formatter: function() {
                        return '<b>' + this.series.name + '</b><br/>' +
                            Highcharts.numberFormat(this.y, 2);
                    }
                },
                legend: {
                    enabled: false
                },
                exporting: {
                    enabled: false
                },
                series: [{
                    name: 'Value',
                    data: function() {
                        var data = [];
                        for (var i = 0; i <= 10; i++) {
                            data.push({
                                x: i - 10,
                                y: 0
                            });
                        }
                        return data;
                    }()
                }]
            });
            return chart;
        }

        Highcharts.setOptions({
            global: {
                DateUTC: false
            }
        });
        add_graph('error', 'Compile errors');
        add_graph('warning', 'Compile warning');
        add_graph('lint', 'Lint warning');
        $('svg > rect').attr('fill', 'none');
    });
};

goog.exportSymbol('main.main', main.main);
