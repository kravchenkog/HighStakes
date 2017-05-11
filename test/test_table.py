from points.points_collector import points_collection





def test_testing(app, func):
    app.cell_new.get_points_collection()
    print(str(111))
#
#
#
# def test_when_game_opened_expected_spin_button_displayd(app, func):
#         #123
#     assert app.game_buttons.spin_button_is_displayed()
#
# def test_when_spin_completed_and_bet_set_expected_rebet_button_is_appears(app, func):
#
#     app.chipselector.selectchip(0)
#     app.cells.tapcel(points_collection, "low_high", 2)
#     app.game_buttons.spin_press()
#     app.wait.round_ends()
#     assert app.game_buttons.rebet_button_is_presented()
#
# def test_when_spin_is_completed_and_bet_is_not_set_expected_rebet_button_is_not_presented(app, func):
#     #app.table.smart_table_to_start_test()
#
#     app.game_buttons.spin_press()
#     app.wait.round_ends()
#     assert not app.game_buttons.rebet_button_is_presented()
#
# def test_when_game_opened_expected_autoplay_button_displayed(app, func):
#
#     assert app.game_buttons.autoplay_button_is_presented()
#
# def test_when_game_opened_expected_settings_button_is_displayed(app, func):
#
#     assert app.game_buttons.settings_button_is_displayed()
#
# def test_when_game_opened_chip_selector_present_and_chips_available(app, func):
#
#     assert app.chipselector.chips_are_displayed()

# def test_when_limit_selected_expected_sorting_of_chips_are_correct(app, func):
#     limits = range(3)
#
#     for limit in limits:
#         app.settings.select_limit_and_save_value(limit) #Low = 0
#         list_of_chips__non_sorted = app.chipselector.get_list_of_chips_values()
#         list_of_chips__sorted = sorted(app.chipselector.get_list_of_chips_values())
#         assert list_of_chips__non_sorted == list_of_chips__sorted
#
# def test_when_round_win_expected_win_popup_presented(app, func):
#
#     app.cells.tapcel(points_collection, "blackred", 2)
#     app.game_buttons.spin_press()
#     app.wait.round_ends()
#
#     assert app.table.win_popup_appears()
#
#
# def test_when_round_not_win_expected_win_popup_not_presented(app, func):
#
#     app.game_buttons.spin_press()
#     app.wait.round_ends()
#
#     assert not app.table.win_popup_appears()
#
# def test_when_game_opened_limits_table_presented(app, func):
#
#     assert app.table.limits_table_presented()
#
# def test_when_limit_selected_expected_values_of_limits_in_table_are_the_same_as_in_settings(app, func):
#
#     list_of_limits = range(3)
#     for limit in list_of_limits:
#         limits_on_settings = app.settings.select_limit_and_save_value(limit)
#         limits_on_table = app.table.get_list_of_limits()
#         assert limits_on_settings == limits_on_table

# def test_when_bet_was_set_expected_clear_button_appears(app, func):
#     app.cells.tapcel(points_collection, "blackred", 1)
#     assert app.game_buttons.clear_button_is_presented()
#
# def test_when_several_bets_are_seted_expexted_clearall_button_appears(app, func):
#     app.settings.select_limit_and_save_value(0)
#     app.chipselector.selectchip(0)
#     app.cells.tapcel(points_collection, "blackred", 2),
#     assert app.game_buttons.clear_all_button_is_presented()
#
# def test_when_all_bets_cleared_expected_clear_clearall_buttons_is_not_presented(app, func):
#     app.settings.select_limit_and_save_value(0)
#     app.chipselector.selectchip(0)
#
#     app.cells.tapcel(points_collection, "number", 5)
#     app.game_buttons.clear_all_tap()
#
#     assert not app.game_buttons.clear_all_button_is_presented()
#     assert not app.game_buttons.clear_button_is_presented()

# def test_when_clear_button_pressed_expected_last_bet_removed(app, func):
#     number_of_first_bets = 5
#     number_of_second_bets = 2
#
#  #   app.settings.select_limit_and_save_value(0)
#     app.chipselector.selectchip(0)
#     app.cells.tapcel(points_collection, "number", number_of_first_bets)
#     list_of_bets = app.table.get_list_of_bets()
#     app.chipselector.selectchip(1)
#     app.cells.tapcel(points_collection, "blackred", number_of_second_bets)
#     list_of_bets_new = app.table.get_list_of_bets()
#
#     assert len(list_of_bets_new) - len(list_of_bets) == number_of_second_bets
#
#     for num in range(number_of_second_bets):
#         app.game_buttons.clear_tap()
#
#     assert list_of_bets == app.table.get_list_of_bets()

# def test_when_set_more_max_per_spot__expected__error_message_appears(app, func):
#     app.settings.select_limit_and_save_value(0)
#     app.chipselector.selectchip(len(app.chipselector.get_list_of_chips())-1) #select max chip
#     app.cells.set_bet_more_max_limit_per_spot(points_collection)
#     assert app.table.popup_is_appeared()
#
# def test_when_set_more_max_per_table__expected__error_message_appears(app, func):
#
#     app.chipselector.selectchip(len(app.chipselector.get_list_of_chips()) - 1)#select max chip
#     app.cells.set_bet_more_max_limit_per_table(points_collection)
#     assert app.table.popup_is_appeared()
#
# def test_when_reber_button_pressed_after_win__expected__win_popup_disappeared(app, func):
#     app.cells.tapcel(points_collection, "blackred", 2)
#     app.game_buttons.spin_press()
#     app.wait.round_ends()
#     app.game_buttons.rebet_button_tap()
#     assert not app.table.win_popup_appears()


