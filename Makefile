# install directory
INSTALL_DIR ?=

# library directory
LIB_DIR ?=

# C compiler
CFLAGS := -Wall -Werror
CFLAGS += -Wno-implicit-function-declaration -Wno-unused-variable
CFLAGS += -Wno-unused-value -Wno-dangling-else -Wno-logical-op-parentheses
CFLAGS += -Wno-empty-body -Wno-missing-braces -Wno-constant-logical-operand
CFLAGS += -Wno-tautological-overlap-compare -Wno-unused-but-set-variable
CFLAGS += -Wno-gnu-folding-constant
CFLAGS += -O3 -fsanitize=address -fsanitize=undefined
CC := clang $(CFLAGS)

# directories
TOP_DIR := $(shell pwd)
TEST_CASES_DIR := $(TOP_DIR)/testcases
BUILD_DIR := $(TOP_DIR)/build

# files
TEST_SRC := $(shell find $(TEST_CASES_DIR) -name '*.c')
TEST_IN := $(shell find $(TEST_CASES_DIR) -name '*.in')

# targets
TEST_EXEC := $(patsubst $(TEST_CASES_DIR)/%.c, $(BUILD_DIR)/%, $(TEST_SRC))
TEST_OUT := $(patsubst $(TEST_CASES_DIR)/%.c, $(BUILD_DIR)/%.out, $(TEST_SRC))
INSTALL_SRC := $(patsubst $(TEST_CASES_DIR)/%.c, $(INSTALL_DIR)/%.c, $(TEST_SRC))
INSTALL_IN := $(patsubst $(TEST_CASES_DIR)/%.in, $(INSTALL_DIR)/%.in, $(TEST_IN))
INSTALL_OUT := $(patsubst $(TEST_CASES_DIR)/%.c, $(INSTALL_DIR)/%.out, $(TEST_SRC))


.PHONY: all install clean check-install-dir check-lib-dir

all: check-lib-dir $(TEST_OUT)

install: check-install-dir check-lib-dir $(INSTALL_SRC) $(INSTALL_IN) $(INSTALL_OUT)

clean:
	-rm -rf $(BUILD_DIR)

check-install-dir:
ifeq ($(INSTALL_DIR),)
	$(error "INSTALL_DIR must be set")
endif

check-lib-dir:
ifeq ($(LIB_DIR),)
	$(error "LIB_DIR must be set")
endif

$(BUILD_DIR)/%.out: $(BUILD_DIR)/% $(TEST_CASES_DIR)/%.in
	mkdir -p $(dir $@)
	$< < $(word 2, $^) > $@; ret=$$?; if [ -z "$$(tail -c 1 "$@")" ]; then echo "$$ret" >> "$@"; else printf "\n$$ret\n" >> "$@"; fi

$(BUILD_DIR)/%.out: $(BUILD_DIR)/%
	mkdir -p $(dir $@)
	$^ > $@; ret=$$?; if [ -z "$$(tail -c 1 "$@")" ]; then echo "$$ret" >> "$@"; else printf "\n$$ret\n" >> "$@"; fi

$(BUILD_DIR)/%: $(TEST_CASES_DIR)/%.c $(LIB_DIR)/libsysy.a
	mkdir -p $(dir $@)
	$(CC) $^ -o $@ -L$(LIB_DIR) -lsysy

$(INSTALL_DIR)/%.c: $(TEST_CASES_DIR)/%.c
	mkdir -p $(dir $@)
	cp $^ $@

$(INSTALL_DIR)/%.in: $(TEST_CASES_DIR)/%.in
	mkdir -p $(dir $@)
	cp $^ $@

$(INSTALL_DIR)/%.out: $(BUILD_DIR)/%.out
	mkdir -p $(dir $@)
	cp $^ $@
