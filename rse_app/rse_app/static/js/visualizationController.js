angular.module('rseApp').controller('visualization', function($scope, $http, $timeout) {	
	$scope.state = 'PENNEE'

	function getRandomArbitrary(min, max) {
	  return Math.random() * (max - min) + min;
	}
	
	var regions = document.getElementById('tooltips');
	
	$scope.drawTooltips = function(data){

		for (var i = 0; i < data.getNumberOfRows(); i++) {
			var html = `<div id="${data.getValue(i, 0)}">`

			for (var j = 1; j < data.getNumberOfColumns(); j++) {
				html += `<p style="font-size:14px">${JSON.parse(data.toJSON()).cols[j].label}: ${data.getFormattedValue(i, j)}</p>`;

			}
			html += `</div>`
			regions.insertAdjacentHTML(
				'beforeEnd', html
			);
		}
	}

	$scope.showMap = function (data, div_id){ 
		google.charts.load('visualization', '1',  {
			'packages': ['geochart'],
			'mapsApiKey': 'AIzaSyCZaPszog934vce2GrxWe3MkgX0mTIx-sE'
		});
		google.charts.setOnLoadCallback(function() { drawRegionsMap(data, div_id); });


		function drawRegionsMap(data, div_id) {

			var data = google.visualization.arrayToDataTable(Object.values(data));

			var options = {
				region: 'ES', // Mexico
				width: 1100, 
				height: 1100,
				resolution: 'provinces',
				colorAxis: {
					values: [100, 100000],
					colors: ['white', 'green']
				},
				backgroundColor: '#006994',
				datalessRegionColor: 'gray',
				defaultColor: '',
				tooltip: {textStyle: {color: 'blue', fontSize: 12}, trigger: 'focus', isHtml: true},
				legend: {textStyle: {color: 'blue', fontSize: 16}}
			};
			var container = document.getElementById(div_id);
			var chart = new google.visualization.GeoChart(container);
			google.visualization.events.addListener(chart, 'select', myClickHandler);

			$scope.drawTooltips(data)
			//	track	events
			var lastEvent = null;
			container.addEventListener('click', function (e) {
				lastEvent = e;
			}, false);
			container.addEventListener('mouseover', function (e) {
				lastEvent = e;
				//	dispatch	click	event	to	get	hover	value
				var event = document.createEvent('SVGEvents');
				event.initEvent('click', true, true);
				e.target.dispatchEvent(event);
			}, false);

			function myClickHandler() {
				var selection = chart.getSelection();
				if (selection.length > 0) {
					if (selection[0].row !== null) {
						if (lastEvent.type === 'mouseover') {
							//	mouseover
							$scope.state = data.getFormattedValue(selection[0].row, 0)
							$scope.$apply()
							console.log($scope.state)
							var regionLinks = regions.getElementsByTagName('div');
							var current_id = data.getValue(selection[0].row, 0);

							for (var i = 0; i < regionLinks.length; i++) {
								var id = regionLinks[i].getAttribute('id');
								regionLinks[i].style.display = (id === current_id) ? 'block' : 'none';
								chart.setSelection([]);
							}
						} else {
							//	click
							alert(data.getFormattedValue(selection[0].row, 0));
							//window.location	=	"/"	+	data.getValue(selection[0].row,	0);
						}
					}
				}
			}
			chart.draw(data, options);

		};
	}

	$scope.showMaps = function (){
		data = [['State', 'Número de contratos', 'Contratos validos'],
				[{f:'Andalucía', v:'ES-AN'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Aragón', v:'ES-AR'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Asturias', v:'ES-AS'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Cantabria', v:'ES-CB'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Castilla La Mancha', v:'ES-CM'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Castilla y León', v:'ES-CL'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Cataluña', v:'ES-CT'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Extremadura ', v:'ES-EX'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Galicia', v:'ES-GA'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Islas Baleares', v:'ES-IB'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'La Rioja', v:'ES-RI'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Madrid', v:'ES-MD'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000), ],
				[{f:'Murcia', v:'ES-MC'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Navarra', v:'ES-NC'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'País Vasco', v:'ES-PV'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Comunidad Valenciana', v:'ES-VC'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Ceuta', v:'ES-CE'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)],
				[{f:'Melilla', v:'ES-ML'},getRandomArbitrary(100, 100000), getRandomArbitrary(100, 100000)]]

		$scope.showMap(data, 'chart_div');

		data_2 = [['State', 'Número de contratos'],	
				[{f:'Canarias', v:'ES-CN'},getRandomArbitrary(100, 100000)]]

		$scope.showMap(data_2, 'canarias_chart_div');
	}

	//Initialization

	$scope.showMaps();
	
})