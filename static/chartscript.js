new Chartist.Line('#temp-chart', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    series: [
      [12, 9, 7, 8, 5]
    ]
  }, {
    fullWidth: true,
    chartPadding: {
      right: 40
    },
    showArea: true,
  }); 


new Chartist.Line('#wind-chart', {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    series: [
      [12, 9, 7, 8, 5]
    ]
  }, {
    fullWidth: true,
    chartPadding: {
      right: 40
    },
    showArea: true,
  }); 