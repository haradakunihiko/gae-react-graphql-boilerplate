'use strict';

const webpack = require('webpack');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const path = require('path');
const merge = require('webpack-merge');

const webpackCommon = {
  entry: {
    app: ['./client/initialize'],
  },
  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: /node_modules/,
        loader: 'babel',
      },
      {
        test: /\.html$/,
        loader: 'underscore-template-loader',
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
      }
    ]
  },
  output: {
    filename: '[name].js',
    path: path.join(__dirname, './public'),
    publicPath: '/public/'
  },
  plugins: [
    new ExtractTextPlugin('app.css'),
    new CopyWebpackPlugin([{
      from: './client/assets/index.html',
      to: './index.html'
    }]),
    new webpack.ProvidePlugin({
      $: 'jquery',
      _: 'underscore'
    })
  ],
  resolve: {
    root: path.join(__dirname, './client')
  },
  resolveLoader: {
    root: path.join(__dirname, './node_modules')
  }
};

switch (process.env.npm_lifecycle_event) {
  case 'start':
  case 'dev':
    module.exports = merge(webpackCommon, {
      devtool: 'inline-source-map',
    });
    break;
  default:
    module.exports = merge(webpackCommon, {
      devtool: 'inline-source-map'
    });
    break;
}
