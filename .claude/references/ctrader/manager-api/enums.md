# Enums

## ProtoOrderType
| Value | Name |
|-------|------|
| 1 | MARKET |
| 2 | LIMIT |
| 3 | STOP |
| 4 | STOP_LOSS_TAKE_PROFIT |
| 5 | MARKET_RANGE |
| 6 | STOP_LIMIT |

## ProtoTradeSide
| Value | Name |
|-------|------|
| 1 | BUY |
| 2 | SELL |

## ProtoTimeInForce
| Value | Name |
|-------|------|
| 1 | GOOD_TILL_DATE |
| 2 | GOOD_TILL_CANCEL |
| 3 | IMMEDIATE_OR_CANCEL |
| 4 | FILL_OR_KILL |
| 5 | MARKET_ON_OPEN |

## ProtoOrderStatus
| Value | Name |
|-------|------|
| 1 | ACCEPTED |
| 2 | FILLED |
| 3 | PARTIALLY_FILLED |
| 4 | CANCELLED |
| 5 | REJECTED |
| 6 | EXPIRED |
| 7 | INACTIVE |

## ProtoDealStatus
| Value | Name |
|-------|------|
| 2 | FILLED |
| 3 | PARTIALLY_FILLED |
| 4 | REJECTED |

## ProtoDealType
| Value | Name |
|-------|------|
| 1 | BUY |
| 2 | SELL |
| 3 | BUY_CANCELLED |
| 4 | SELL_CANCELLED |
| 5 | BALANCE_DEPOSIT |
| 6 | BALANCE_WITHDRAWAL |
| 7 | BONUS_DEPOSIT |
| 8 | BONUS_WITHDRAWAL |
| 9 | INITIAL_DEPOSIT |
| 10 | INITIAL_LOAD |
| 11 | AUTO_ROLLOVER_CLOSE |
| 12 | AUTO_ROLLOVER_OPEN |
| 34 | SWAP |
| 35 | COMMISSION |

## ProtoPositionStatus
| Value | Name |
|-------|------|
| 1 | OPEN |
| 2 | CLOSED |
| 3 | CREATED |

## ProtoBookType
| Value | Name |
|-------|------|
| 1 | BOOK_A |
| 2 | BOOK_B |

## ProtoAccountType
| Value | Name |
|-------|------|
| 1 | HEDGED |
| 2 | NETTED |

## ProtoAccessRights
| Value | Name |
|-------|------|
| 1 | FULL_ACCESS |
| 2 | CLOSE_ONLY |
| 3 | NO_TRADING |
| 4 | NO_LOGIN |

## ProtoCrudOperation
| Value | Name |
|-------|------|
| 1 | CREATE |
| 2 | UPDATE |
| 3 | DELETE |

## ProtoChangeBalanceType
| Value | Name |
|-------|------|
| 0 | BALANCE_DEPOSIT |
| 1 | BALANCE_WITHDRAW |
| 2 | BONUS_DEPOSIT |
| 3 | BONUS_WITHDRAW |
| 4 | INITIAL_DEPOSIT |
| 5 | INITIAL_LOAD |
| 6 | REVERSE_BALANCE_DEPOSIT |
| 7 | REVERSE_BALANCE_WITHDRAWAL |
| 8 | BONUS_CANCEL |
| 9 | MANAGER_BONUS_DEPOSIT |
| 10 | MANAGER_BONUS_WITHDRAW |

## ProtoOrderTriggerMethod
| Value | Name |
|-------|------|
| 1 | TRADE |
| 2 | OPPOSITE |
| 3 | DOUBLE_TRADE |
| 4 | DOUBLE_OPPOSITE |

## ProtoTotalMarginCalculationType
| Value | Name |
|-------|------|
| 1 | MAX |
| 2 | SUM |
| 3 | NET |

## ProtoManagerPermission
| Value | Name |
|-------|------|
| 1 | TRADE |
| 2 | ACCOUNT |
| 3 | HISTORY |
| 4 | REPORTING |
| 5 | SETTINGS |
| 6 | DEALING |
| 7 | LP |
| 8 | ADMIN |
