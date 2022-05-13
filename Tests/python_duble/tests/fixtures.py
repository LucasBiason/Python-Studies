import pytest

@pytest.fixture
def resultado_em_duas_paginas():
    return [
        """
        {
            "num_docs": 5,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 5,
            "docs": [
                {"author": "Kenneth Reitz",
                 "title": "O Guia do Mochileiro Python"
                },
                 {"author": "Wes McKinney",
                 "title": "Python Para Análise de Dados"
                }
            ]
        }
        """,
    ]


@pytest.fixture
def resultado_em_tres_paginas():
    return [
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Kenneth Reitz",
                 "title": "O Guia do Mochileiro Python"
                },
                 {"author": "Wes McKinney",
                 "title": "Python Para Análise de Dados"
                }
            ]
        }
        """,
    ]


@pytest.fixture
def conteudo_de_4_arquivos():
    return [
        """
        {
            "num_docs": 17,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 17,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]

        }
        """,
        """
        {
            "num_docs": 17,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 17,
            "docs": [
                {"author": "Kenneth Reitz",
                 "title": "O Guia do Mochileiro Python"
                },
                 {"author": "Wes McKinney",
                 "title": "Python Para Análise de Dados"
                }
            ]
        }
        """,
    ]


@pytest.fixture
def resultado_em_tres_paginas_erro_na_pagina_2():
    return [
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        None,
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Kenneth Reitz",
                 "title": "O Guia do Mochileiro Python"
                },
                 {"author": "Wes McKinney",
                 "title": "Python Para Análise de Dados"
                }
            ]
        }
        """,
    ]


@pytest.fixture
def resultado_em_tres_paginas_erro_na_pagina_1():
    return [
        None,
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Luciano Ramalho",
                 "title": "Python Fluente"
                },
                {"author": "Nilo Ney",
                 "title": "Introdução a Programação com Python"
                },
                 {"author": "Allen B. Downey",
                 "title": "Pense em Python"
                }
            ]
        }
        """,
        """
        {
            "num_docs": 8,
            "docs": [
                {"author": "Kenneth Reitz",
                 "title": "O Guia do Mochileiro Python"
                },
                 {"author": "Wes McKinney",
                 "title": "Python Para Análise de Dados"
                }
            ]
        }
        """,
    ]

