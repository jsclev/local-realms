const VueLoaderPlugin = require('vue-loader/lib/plugin');

const path = require('path');

module.exports = {
    entry: './static/js/app/main.js',
    mode: 'development',
    resolve: {
        alias: {
            'vue$': 'vue/dist/vue.esm.js'
        }
    },
    output: {
        path: path.resolve(__dirname, 'static/js/dist'),
        filename: 'main.js'
    },
    module: {
        rules: [{
            test: /\.vue$/,
            loader: 'vue-loader'
        }, {
            test: /\.css$/,
            use: [
                'vue-style-loader',
                'css-loader'
            ]
        }]
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    watch: true
};
