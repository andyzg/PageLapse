module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      build: {
        src: ['assets/js/script.js'],
        dest: 'static/js/script.js',
        nonull: true,
      },
      lib: {
        src: ['assets/lib/js/*.js'],
        dest: 'static/js/lib.js',
        nonull: true,
      },
    },
    uglify: {
      build: {
        src: '<%= concat.build.dest %>',
        dest: 'static/js/script.min.js'
      },
      lib: {
        src: '<%= concat.lib.dest %>',
        dest: 'static/js/lib.min.js'
      }
    },
    clean: {
      build: {
        src: ['<%= concat.build.dest %>'],
      },
      lib: {
        src: ['<%= concat.lib.dest %>']
      }
    },
    sass: {
      dist: {
        files: {
          'static/css/style.css': 'assets/scss/style.scss',
        }
      }
    },
    watch: {
      js: {
        files: ['assets/js/*'],
        tasks: ['js']
      },
      scss: {
        files: ['assets/scss/*'],
        tasks: ['sass']
      }
    }
  });

  // Load the plugin that provides the 'uglify' task.
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-sass');

  // grunt.registerTask('lib', ['concat:lib', 'uglify:lib', 'clean:lib']);
  grunt.registerTask('lib', ['concat:lib']);


  // grunt.registerTask('js', ['concat:build', 'uglify:build', 'clean:build']);
  grunt.registerTask('js', ['concat:build']);
};
