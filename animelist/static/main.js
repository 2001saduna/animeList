document.addEventListener('DOMContentLoaded', function() {
    var animeItems = document.querySelectorAll('.anime-item');

    animeItems.forEach(function(item) {
        item.addEventListener('mouseover', function() {
            var description = this.querySelector('.anime-description');
            if (description) {
                description.classList.remove('hidden');
                description.classList.add('shown');
            }
        });

        item.addEventListener('mouseout', function() {
            var description = this.querySelector('.anime-description');
            if (description) {
                description.classList.remove('shown');
                description.classList.add('hidden');
            }
        });
    });
});
