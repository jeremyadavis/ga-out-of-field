import { withRouter } from 'next/router';
import fetch from 'isomorphic-unfetch';

const Post = withRouter(props => (
  <div>
    <h1>{props.show.name}</h1>
    <p>{props.show.summary.replace(/<[/]?p>/g, '')}</p>
    <img src={props.show.image.medium} />

    <style jsx>
      {`
        h1,
        a {
          font-family: 'Arial';
          color: blue;
        }

        ul {
          padding: 0;
        }

        li {
          list-style: none;
          margin: 5px 0;
        }

        p {
          font-size: 3em;
        }

        a {
          text-decoration: none;
          color: blue;
        }

        a:hover {
          opacity: 0.6;
        }
      `}
    </style>
  </div>
));

Post.getInitialProps = async function(context) {
  const { id } = context.query;
  const res = await fetch(`https://api.tvmaze.com/shows/${id}`);
  const show = await res.json();

  console.log('Fetched show: ', show.name);

  return { show };
};

export default Post;
