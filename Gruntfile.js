module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      build: {
        options: {
          separator: ';',
        },
        dist: {
          src: ['assets/js/*.js'],
          dest: 'static/js/script.js'
        },
      },
      lib: {
        options: {
          separator: ';',
        },
        dist: {
          src: ['assets/lib/js/*.js'],
          dest: 'static/js/lib.js'
        }
      },
    },
    uglify: {
      build: {
        src: '<%= concat.build.dist.dest %>',
        dest: 'static/js/script.min.js'
      },
      lib: {
        src: '<% concat.lib.dist.dest %>',
        dest: 'static/js/lib.min.js'
      }
    },
    clean: {
      build: {
        src: ['<%= concat.build.dist.dest %>'],
      },
      lib: {
        src: ['<%= concat.lib.dist.dest %>']
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
        tasks: ['concat:build', 'uglify:build', 'clean:build']
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

  grunt.registerTask('lib', ['concat:lib', 'clean:lib']);
};
