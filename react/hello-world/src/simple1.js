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


function Container(){
    const [count, setCount] = React.useState(0);
    return (
        <div>
        <LikeButton/>
        <div style={{marginTop:20}}>
            <span>현재카운트</span>
        <span style={{marginRight : 10}}>{count}</span>
        <button onClick={()=> setCount(count +1)}>증가</button>
        <button onClick={()=> setCount(count -1)}>
            감소!</button>
            </div>
        </div>

    )
};


const domContainer = document.getElementById('root');
ReactDOM.render(React.createElement(Container), domContainer)