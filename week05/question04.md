# 연결리스트(Linked List)
아래 설명을 먼저 읽어주세요. 
linked list에 대한 설명입니다.
https://community.wecode.co.kr/t/linked-list/1175

Singly Linked List
singly linked list에 대해 조금 더 자세히 알아보겠습니다.
위의 stack overflow 설명과 같이, singly-linked list는 특정 index의 node value를 바로 얻을 수가 없습니다.

만약 i번째 요소를 얻고 싶으면 head node부터 node를 하나하나 탐색해야 알 수 있습니다.
예를 들어 head의 node가 23이라고 할 때, 3번째 node를 알고 싶으면 head의 next 값을 알아서 -> 2번째 node를 알아서 -> 2번째 node를 방문해야만 3번째 node를 알 수 있습니다.

2번째 node가 6이라고 한다면 head node 23의 next는 6이었을 것이고, 다시 6을 방문해 next 값을 얻는 식으로 하나하나 거치며 도달할 수 있습니다.

이렇게 array에 비교해 비효율적이어 보이는 linked list를 왜 쓸까 궁금해 할 수 있겠지만,insert, delete의 기능을 추가한 linked list를 직접 설계할 수 있다면 마치 array를 사용하는 것처럼 편할 것입니다.

# 코드 카타
linked list를 만들 수 있는 MyLinkedList 클래스를 설계해봅시다.
singly linked list 로 해도 되고, doubly linked list 로 구현하셔도 됩니다.

singly linked list를 구현하려면 val과 next라는 속성이 있어야 합니다.
val: 현재 node의 value
next: 다음 node를 가르키는 pointer(reference)

doubly linked list를 구현하려면 prev라는 속성이 하나 더 있어야 합니다.
prev: 이전 node를 가르키는 pointer(reference)

MyLinkedList 클래스에는 5가지 method가 있습니다.
아래의 설명을 참고하여 구현해주세요.

- get(index) : linked list 의 index 번째 node의 value를 return해주세요. 값이 없으면 -1을 return해주세요.

- addAtHead(val) : linked list 의 첫 번째 요소 전에 value가 val인 node를 추가해주세요. val이 추가되면 이 node는 linked list의 첫 번째 노드가 되는 것입니다.

- addAtTail(val) : value가 val인 node를 linked list의 마지막에 추가해주세요.

- addAtIndex(index, val) : value가 val인 node를 linked list의 index node 바로 전에 추가해주세요. 만약 index가 linked list의 길이와 같다면 제일 마지막에 추가하면 됩니다. 만약 index가 길이보다 길다면, node를 추가하지 말아주세요.

- deleteAtIndex(index) : linked list의 index 번째 node를 삭제해주세요.

```
MyLinkedList 클래스는 아래와 같이 사용됩니다.

linkedList = MyLinkedList()
linkedList.addAtHead(1)
linkedList.addAtTail(3)
linkedList.addAtIndex(1, 2)  // linked list는 1->2->3 가 됩니다.
linkedList.get(1)            // returns 2
linkedList.deleteAtIndex(1)  // linked list는 이제 1->3
linkedList.get(1)            // returns 3
```
