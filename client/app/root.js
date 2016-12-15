import React from 'react'
import GraphiQL from 'graphiql';
import fetch from 'isomorphic-fetch';

function graphQLFetcher(graphQLParams) {

  return fetch(window.location.origin + '/graphql', {
    method: 'post',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(graphQLParams),
  }).then(response => response.json());
}

export default () => {
  return (
    <GraphiQL fetcher={graphQLFetcher} />
  )
}
