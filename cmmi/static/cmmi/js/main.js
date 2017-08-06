
var ProyectosListPage = {
	init: function() {
		this.$container = $('.proyectos-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-urgente', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-exclamation-sign', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

var TareasListPage = {
	init: function() {
		this.$container = $('.tareas-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-urgente', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-exclamation-sign', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};

$(document).ready(function() {
	ProyectosListPage.init();
	TareasListPage.init();
});
