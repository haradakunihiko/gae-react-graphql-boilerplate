# Graphql playground

served at https://graphql-libtech.appspot.com/

This is a modern JS skeleton with MarionetteJS for [Webpack](https://webpack.github.io/).

## Getting started

* Install:
    * Inside this folder run: `npm install` and `grunt pip:shell`
* Build javascript:
    * `npm run build` - builds you project
    * `npm run watch` - watch you project
* Start
	* start your appengine server
* Restore data
    * `grunt gae:downlaod` and `grunt gae:upload` to resotre data (or use datastore.db downloaded from tablish-dev.)
* Learn:
    * `public/` dir is fully auto-generated and served by HTTP server.  Write your code in `client/` dir.

# GraphQL examples

see https://gitlab.com/libtech/graphql/blob/master/server/schema.py for GraphQL schema definition.

## fetch all user and their copies with edition/book.

```
{
  users {
    ndbId
    name
    copies {
      edition {
        ndbId
        title
        book {
          title
        }
      }
	}
  }
}

```

## fetch using search index.

```

{
  users(query: "libtech") {
    name
    email
    detail
	}
}
```


## fetch specific user.

```
{
  user(id: "me") {
    ndbId
    name
    copies {
      edition {
        ndbId
        title
        book {
          title
        }
      }
	}
  }
}

```

```
{
  user(id: "4659893755707392") {
    ndbId
    name
    copies {
      edition {
        ndbId
        title
        book {
          title
        }
      }
	}
  }
}

```

## fetch all groups

```
{
  groups {
    name
  }
}
```

## fetch 'me' (query does not need to be model name.)

```

{
  me {
    name
    email
    detail
  }
}
```