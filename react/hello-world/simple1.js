function LikeButton(){
    // likebutton에 liked라는 상태값을 추가
    const [liked, setLiked] = React.useState(false);
    const text = liked ? '좋아요 취소' : '좋아요';

    return React.createElement(
        'button',
        { onClick: () => setLiked(!liked)},
        text,     
    )
}

const domContainer = document.getElementById('root');
ReactDOM.render(React.createElement(LikeButton), domContainer);