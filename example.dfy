function Sum(n: nat): nat
{
    if n == 0 then 0 else n + Sum(n-1)
}

method ComputeSum(n: nat) returns (s: nat)
    ensures s == Sum(n)
{
    s := 0;
    var i := 0;
    while (i < n)
        invariant 0 <= i <= n
        invariant s == Sum(i)
    {
        i := i + 1;
        s := s + i;
    }
}


function Fib(n: nat): nat
{
    if (n < 2) then n else (Fib(n-1) + Fib(n-2))
}

method ComputeFib(n: nat) returns (x: nat)
    ensures x == Fib(n)
{
    x := 0;
    var y := 1;
    var i := 0;
    ghost var ghost_unused := 0;

    while (i < n)
        invariant 0 <= i <= n
        invariant x == Fib(i) && y == Fib(i+1)
        decreases n - i
    {
        x, y := y, x + y;
        i := i + 1;
    }
}

method Main() {
    var i := 0;
    while (i < 6) {
        var tmp := ComputeSum(i);
        print "Sum ", i, ": ", tmp, "\n";
        i := i + 1;
    }
}


predicate sorted(s: seq<int>)
{
    forall i, j :: 0 <= i < j < |s| ==> s[i] <= s[j]
}


lemma multisetContains(a: seq<int>, b: seq<int>, x: int)
    requires multiset(a) == multiset(b)
    requires x in a
    ensures x in b
{
    var m: multiset<int> := multiset(a);
    assert x in m;
}

datatype Tree = Leaf | Node(Tree, int, Tree)

trait Animal {
}

class {: autocontracts} Dog extends Animal {
    var name: string
    var barkCount: nat

    constructor (name: string)
    requires name != ""
    //ensures Valid() // added automatically via autocontracts
    {
        this.name := name;
        this.barkCount := 0;
    }

    ghost predicate Valid()
    reads this`name, this`barkCount
    {
        this.name != "" && this.barkCount >= 0
    }

    method bark() returns ()
    modifies this`barkCount
    {
        print this.name, ": woof\n";
        this.barkCount := this.barkCount + 1;
    }
}

lemma DisjointIntersectionLemma<T(!new)>(A: set<T>, B: set<T>)
    requires A * B == {}
    ensures A !! B
{
    forall x | x in A ensures x !in B
    {
        if x in B
        {
            assert x in A * B;
        }
    }
}

datatype BYTree = BlueLeaf
                | YellowLeaf
                | Node(left: BYTree, right: BYTree)

function LeftDepth'(t: BYTree): nat
{
    if t.Node? then 1 + LeftDepth'(t.left)
    else 0
}
