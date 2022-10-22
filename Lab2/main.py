from symboltable import SymbolTable

if __name__ == '__main__':
    st = SymbolTable(13)
    identifiers = ["a", "b", "cc", "de"]
    constants = ["ab", "123", "gf6", "89j"]

    for elem in identifiers:
        st.insert(elem)

    for elem in constants:
        st.insert(elem)
    print(st)

    assert (st.search("de"))
    assert (st.get_value_on_position(10, 0) == "a")
    assert (st.get_index("gf6") == 2)

    st.delete("b")
    assert (st.search("b") is False)
