def test_library_urls():
    try:
        from library.urls import urlpatterns as solution_urlpatterns # type: ignore
    except Exception as e:
        raise AssertionError(
            'При импорте списка маршрутов `urlpatterns` из файла '
            f'`library/urls.py` произошла ошибка: {e}'
        ) from e
    assert isinstance(solution_urlpatterns, list), (
        'Убедитесь, что значением переменной `urlpatterns` является список.'
    )
    assert len(solution_urlpatterns) >= 3, (
        'Убедитесь, что к головному списку `urlpatterns` подключены маршруты '
        'из файла `library/urls.py`.'
    )


def test_pages_urls():
    try:
        from pages.urls import urlpatterns as solution_urlpatterns # type: ignore
    except Exception as e:
        raise AssertionError(
            'При импорте списка маршрутов `urlpatterns` из файла '
            f'`pages/urls.py` произошла ошибка: {e}'
        ) from e
    assert isinstance(solution_urlpatterns, list), (
        'Убедитесь, что значением переменной `urlpatterns` из файла '
        '`pages/urls.py` является список.'
    )
    assert len(solution_urlpatterns) == 1, (
        'Убедитесь, что к головному списку `urlpatterns` подключены маршруты '
        'из файла `pages/urls.py`.'
    )


def test_catalog_urls():
    try:
        from catalog.urls import urlpatterns as solution_urlpatterns # type: ignore
    except Exception as e:
        raise AssertionError(
            'При импорте списка маршрутов `urlpatterns` из файла '
            f'`catalog/urls.py` произошла ошибка: {e}'
        ) from e
    assert isinstance(solution_urlpatterns, list), (
        'Убедитесь, что значением переменной `urlpatterns` из файла '
        '`catalog/urls.py` является список.'
    )
    assert len(solution_urlpatterns) == 2, (
        'Убедитесь, что к головному списку `urlpatterns` подключены маршруты '
        'из файла `catalog/urls.py`.'
    )
